import { SetStateAction, useState } from "react";

type Props = {};
import Login from "./Login/Login";
import Register from "./Register/Register";
const AutorizationPage = (props: Props) => {
  const [activeTab, setActiveTab] = useState("login"); // Initially active tab is "login"

  const handleTabChange = (tab: SetStateAction<string>) => {
    setActiveTab(tab);
  };
  return (
    <div className="autorization-page">
      <div className="autorization_inner">
        <div className="autorize_header">
          <span
            onClick={() => handleTabChange("login")}
            className={activeTab === "login" ? "active" : ""}
          >
            Login
          </span>
          <span
            onClick={() => handleTabChange("register")}
            className={activeTab === "register" ? "active" : ""}
          >
            Register
          </span>
        </div>
        <div className="autorize_form">
          {activeTab === "login" ? <Login /> : <Register />}
        </div>
      </div>
    </div>
  );
};

export default AutorizationPage;
