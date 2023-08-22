import { Suspense } from "react";
import { Route, Routes, Navigate } from "react-router-dom";
import AdminPage from "../pages/AdminPage/AdminPage";
import ConstructorPage from "../pages/ConstructorPage/ConstructorPage";
import HelpPage from "../pages/HelpPage/HelpPage";
import MainPage from "../pages/MainPage/MainPage";
import NotFound from "../pages/NotFound/NotFound";
import NotificationPage from "../pages/NotificationPage/Notification";
import RegistersPage from "../pages/RegistersPage/RegistersPage";
import ReportPage from "../pages/ReportPage/ReportPage";
import Loader from "../widgets/Loader/Loader";
import Navbar from "../widgets/Navbar/Navbar";
type Props = {}

const AppRoutes = (props: Props) => {
  return (
    <>
  <Suspense fallback={<Loader />}>
    <Navbar />
    <Routes>
      <Route path="/" element={<MainPage />} />
      <Route path="/notification" element={<NotificationPage />} />
      <Route path="/reports" element={<ReportPage />} />
      <Route path="/registers" element={<RegistersPage />} />
      {/* <Route path="/visualization" element={<VisualizationPage />} /> */}

        <Route path="/admin" element={<AdminPage />} />
        <Route path="/constructor" element={<ConstructorPage />} />
        <Route path="/help" element={<HelpPage />} />
    
      <Route path="*" element={<NotFound />} />
    </Routes>
    </Suspense>
  </>
  )
}

export default AppRoutes