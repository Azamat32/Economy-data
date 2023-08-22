
import "./Navbar.scss"
import logo from "../../assets/Gallery/logo.png"
type Props = {}

const Navbar = (_props: Props) => {
  return (
    <div className="navbar">
      <div className="container">
        <div className="nav_inner">
        <div className="nav_logo">
            <a href="{% url 'index'  %}">
              <div className="nav_logo_img">
                <img
                  src={logo}
                  alt="Фото в подвале"
                  className="width: 100%; height: auto"
                />
              </div>
            </a>
          </div>

          <div className="nav_download">
            <a href="{% static 'doc/DocForPresetation.docx' %}">Скачать файл</a>
            <a href="{% static 'doc/DocForPresetation.docx' %}"
              >Сформировать шаблон</a
            >
          </div>
        </div>
      </div>
    </div>
  )
}

export default Navbar