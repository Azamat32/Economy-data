import  { useState } from 'react';

const Register = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [registrationStatus, setRegistrationStatus] = useState("notRegistered");

  const handleRegister = async () => {
    if (password !== confirmPassword) {
      alert('Passwords do not match.');
      return;
    }

    try {
      const response = await fetch('http://localhost:5000/api/user/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, email, password }),
      });

      if (response.ok) {
        setRegistrationStatus('success');
      } else {
        setRegistrationStatus('error');
      }
    } catch (error) {
      console.error('An error occurred:', error);
      setRegistrationStatus('error');
    }
  };

  return (
    <div className="Register">
      <h2>Register</h2>
      {registrationStatus === 'success' ? (
        <p>Registration successful! You can now log in.</p>
      ) : (
        <div className='form_group'>
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
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
          <input
            type="password"
            placeholder="Confirm Password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
          />
          <button onClick={handleRegister}>Register</button>
          {registrationStatus === 'error' && (
            <p>Registration failed. Please try again later.</p>
          )}
        </div>
      )}
    </div>
  );
};

export default Register;
