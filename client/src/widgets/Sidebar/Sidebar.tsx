import { NavLink } from "react-router-dom";
import "./Sidebar.scss";
type SideBarProps = {
  SideBarState:boolean
};

const Sidebar = (props: SideBarProps) => {
  const {SideBarState} = props
  return (
    <div className={`sidebar ${SideBarState ? "open" : ""}`}>
      <div className="sidebar_inner">
        <ul>
          <li>
            <NavLink to="/">MainPage </NavLink>
          </li>
          <li>
            <NavLink to="/notification">Notifications </NavLink>
          </li>
          <li>
            <NavLink to="/reports">Reports </NavLink>
          </li>

          <li><NavLink to="/registers">Реестры </NavLink></li>
    <li>      <NavLink to="/admin">Администрирование </NavLink></li>
         <li> <NavLink to="/constructor">Конструктор форм и запросов </NavLink></li>
     <li>     <NavLink to="/help">Помощь </NavLink></li>
         
        </ul>
      </div>
    </div>
  );
};

export default Sidebar;
