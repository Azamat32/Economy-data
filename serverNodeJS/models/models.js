const { DataTypes } = require("sequelize");

const sequelize = require("../db");

const User = sequelize.define("users", {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  email: {
    // Add this new property for the email column
    type: DataTypes.STRING,
    allowNull: false, // or false if email is required
    unique: true, // If you want emails to be unique
  },

  username: {
    type: DataTypes.STRING,
    allowNull: true,
  },
  password: {
    type: DataTypes.STRING,
    allowNull: true,
  },
  role: {
    type: DataTypes.STRING,
    allowNull: false,
    defaultValue: "Обычный пользователь",
  },
});

module.exports = {
  User,
};
