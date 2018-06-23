export default {
  name: 'InnerHeaderComponent',
  props: ['title'],
  data: () => ({
    menu: false,
    notifications: null,
    unread: false
  }),
  watch: {
    $route() {
      var root = this
      this.$auth.get_notifications(root)
    }
  },
  methods: {
    notification_icon(type) {
      switch (type) {
        case 1:
          return 'alternate_email'
        case 2:
          return 'reply'
        case 4:
          return 'edit'
        case 5:
          return 'favorite'
        case 6:
          return 'email'
        case 9:
          return 'reply'
        case 11:
          return 'link'
        default:
          return 'notifications'
      }
    }
  },
  mounted() {
    var root = this
    this.$auth.get_notifications(root)
  }
}
