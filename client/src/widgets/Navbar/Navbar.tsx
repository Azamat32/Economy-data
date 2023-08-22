import "./Navbar.scss";
import logo from "../../assets/Gallery/logo.png";
import Sidebar from "../Sidebar/Sidebar";
import { useState } from "react";
type Props = {};

const Navbar = (_props: Props) => {
  const [isOpen, setIsOpen] = useState(false);

  const handleBasketClose = () => {
    setIsOpen(!isOpen);
  };
  return (
    <div className="navbar">
      <div className="container">
        <div className="nav_inner">
          <div
            className={`nav_btn ${isOpen ? "active" : ""}`}
            onClick={handleBasketClose}
          >
            <span></span>
          </div>
          <div className="nav_logo">
            <a href="">
              <div className="nav_logo_img">
                <img
                  src={logo}
                  alt="Фото в подвале"
                  className="width: 100%; height: auto"
                />
              </div>
            </a>
          </div>

          <div className="nav_text">
            <p>АО «Институт экономических исследований</p>
            <p>Цифровая экосистема ERI</p>
          </div>
        </div>
      </div>
      <Sidebar SideBarState={isOpen} />
    </div>
  );
};

export default Navbar;
