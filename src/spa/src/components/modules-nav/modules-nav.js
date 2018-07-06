export default {
  name: 'ModulesNavComponent',
  components: {},
  data: () => ({
    current: {
      module: {}
    }
  }),
  props: ['modules'],
  created() {
    if (typeof this.$route.params.module !== 'undefined') {
      this.current.module = this.$api.getModuleId(this.modules)
    } else {
      this.current.module = this.modules[0]
    }
  },
  methods: {
    isComplete(module) {
      let complete = true
      for (let i = 0; i < module.lessons.length; i++) {
        if (module.lessons[i].is_shown === false) {
          complete = false
          break
        }
      }
      return complete
    },
    getLessonAction(type) {
      switch (type) {
        case '0':
          return 'play_arrow'
        case '1':
          return 'play_arrow'
        case '2':
          return 'menu'
        case '3':
          return 'star'
        case '4':
          return 'build'
      }
    }
  }
}
