const { defineConfig } = require("cypress");

module.exports = defineConfig({
  projectId: 'c2k8z7',
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
