const Router = require("express");
const router = new Router();
const userControllers = require("../controllers/userController");

router.post("/login", userControllers.Login);
router.post("/register", userControllers.Register);

module.exports = router;
