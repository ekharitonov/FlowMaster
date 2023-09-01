// 4. API Calls from React to Flask:
// Fetching data from the Flask backend:

import React, { useState, useEffect } from 'react';

function DataComponent() {
  const [data, setData] = useState({});

  useEffect(() => {
    fetch('/api/data')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  return (
    <div>
      <h1>Data from Backend: {data.message}</h1>
    </div>
  );
}