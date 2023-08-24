"use strict";

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.addColumn("users", "email", {
      type: Sequelize.STRING,
      allowNull: false, // or false if email is required
      unique: true, // If you want emails to be unique
    });
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.removeColumn("users", "email");
  },
};
