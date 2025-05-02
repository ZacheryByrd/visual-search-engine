import React, { useState } from 'react';
import './App.css';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [matches, setMatches] = useState([]);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!selectedFile) return;

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await fetch('http://localhost:5000/upload', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      setMatches(data.matches);
    } catch (error) {
      console.error('Error uploading image:', error);
    }
  };

  return (
    <div className="App" style={{ padding: '40px', fontFamily: 'Arial' }}>
      <h1 style={{ marginBottom: '30px' }}>🔍 Visual Search Engine</h1>
  
      <form onSubmit={handleSubmit} style={{ marginBottom: '30px' }}>
        <input type="file" onChange={handleFileChange} style={{ marginRight: '10px' }} />
        <button type="submit" style={{ padding: '6px 14px', cursor: 'pointer' }}>
          Upload Image
        </button>
      </form>
  
      <h2>Matches:</h2>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '20px', marginTop: '20px' }}>
        {matches.map((match, index) => (
          <div key={index} style={{
            border: '1px solid #ccc',
            borderRadius: '8px',
            padding: '10px',
            width: '160px',
            textAlign: 'center',
            boxShadow: '0 2px 6px rgba(0,0,0,0.1)'
          }}>
            <img
              src={match.image_url}
              alt={`match-${index}`}
              width="140"
              height="140"
              style={{ borderRadius: '4px', objectFit: 'cover' }}
            />
            <div style={{ marginTop: '8px', fontSize: '14px' }}>
              Label: {match.label}
            </div>
          </div>
        ))}
      </div>
    </div>
  );  
}

export default App;
