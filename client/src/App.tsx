import { useState, useEffect } from 'react'

import './App.css'
import MainPage from './pages/MainPage/MainPage';
import Navbar from './widgets/Navbar/Navbar';
function App() {
  const [data, setData] = useState([])
  console.log(data);
  
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
