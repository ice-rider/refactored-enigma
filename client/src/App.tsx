import React from 'react';
import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Main from './pages/Main';
import Login from './pages/Login';
import 'react-toastify/dist/ReactToastify.css';
import { ToastContainer } from 'react-toastify';
import axios from 'axios';

function App() {

  axios.defaults.baseURL = 'https://turbo-cod-g9x9p46jjpr2v74g-5000.app.github.dev/api'

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" Component={Main}/>
          <Route path="/login" Component={Login}/>
        </Routes>
      </BrowserRouter>
      <ToastContainer 
        position="bottom-right"
        autoClose={5000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
        theme="colored"/> 
    </>
  );
}

export default App;
