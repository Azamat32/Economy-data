const jwt = require("jsonwebtoken");
const bcrypt = require("bcrypt");
require("dotenv").config();

const { User } = require("../models/models");

exports.Login = async (req, res, next) => {
  try {
    const { email, password } = req.body;
    const user = await User.findOne({ where: { email } });
    if (!user) {
      return res.status(404).json({ message: "User not found" });
    }
    const isPasswordValid = await bcrypt.compare(password, user.password);
    if (!isPasswordValid) {
      return res.status(401).json({ message: "Invalid password" });
    }

    // Generate a JWT token
    const token = jwt.sign({ userId: user.id }, process.env.JWT_SECRET, {
      expiresIn: "1h", // Token expiration time
    });

    res.json({ token });
  } catch (error) {
    console.log(error);
    res.json.status(500).send({ message: error.message });
  }
};

exports.Register = async (req, res, next) => {
  try {
    const { username, password, email, confirmPassword } = req.body;
    // Check if the passwords match
    if (password !== confirmPassword) {
      return res.status(400).json({ message: "Passwords do not match" });
    }

    // Hash the password
    const hashedPassword = await bcrypt.hash(password, 10);

    // Create a new user
    const newUser = await User.create({
      username,
      password: hashedPassword,
      email,
      role: "Обычный пользователь", // Default role
    });

    res.status(201).json({ message: "User registered successfully" });
  } catch (error) {
    console.log(error);
    res.json.status(500).send({ message: error.message });
  }
};
