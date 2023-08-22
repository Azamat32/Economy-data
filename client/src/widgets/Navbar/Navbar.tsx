import "./Navbar.scss";
import logo from "../../assets/Gallery/logo.png";
type Props = {};

const Navbar = (_props: Props) => {
  return (
    <div className="navbar">
      <div className="container">
        <div className="nav_inner">
          <div className="nav_btn">
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
            <p>
              АО «Институт экономических исследований 
            </p>
            <p>
               Цифровая экосистема ERI
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Navbar;
