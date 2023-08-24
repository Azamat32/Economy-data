import { useState } from 'react';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogin = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/user/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });
  
      if (response.ok) {
        setIsLoggedIn(true);
      } else {
        setIsLoggedIn(false);
        alert('Invalid email or password');
      }
    } catch (error) {
      console.error('An error occurred:', error);
      setIsLoggedIn(false);
      alert('An error occurred. Please try again later.');
    }
  };
  

  return (
    <div className="Login">
      <h2>Login</h2>
      {isLoggedIn ? (
        <div>
          <p>Welcome, user!</p>
        </div>
      ) : (
        <div className='form_group'>
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button onClick={handleLogin}>Login</button>
        </div>
      )}
    </div>
  );
};

export default Login;
