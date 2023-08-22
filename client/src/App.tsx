import {  useEffect } from 'react'

import './App.css'
import MainPage from './pages/MainPage/MainPage';
import Navbar from './widgets/Navbar/Navbar';
function App() {
  
  useEffect(() => {
   
  }, [])

  return (
    <>
     <Navbar />
     <MainPage />
    </>
  )
}

export default App
