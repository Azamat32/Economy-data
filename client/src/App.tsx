import {  useEffect } from 'react'
import { BrowserRouter } from "react-router-dom";

import './App.css'
import AppRoutes from './Routes/AppRoutes';
function App() {
  
  useEffect(() => {
   
  }, [])

  return (
    <>
      <BrowserRouter>
        <AppRoutes />
      </BrowserRouter>
    </>
  )
}

export default App
