import {  useEffect } from 'react'
import { BrowserRouter } from "react-router-dom";
import { QueryClient, QueryClientProvider } from 'react-query';

import './App.css'
import AppRoutes from './Routes/AppRoutes';
function App() {
  

  const queryClient = new QueryClient();

  return (
    <>
     <QueryClientProvider client={queryClient}>
     <BrowserRouter>
        <AppRoutes />
      </BrowserRouter>
     </QueryClientProvider>
 
    </>
  )
}

export default App
