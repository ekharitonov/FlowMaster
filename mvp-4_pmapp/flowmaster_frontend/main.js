// main.js
const { useState } = React;

function App() {
  const [attributes, setAttributes] = useState({});

  const handleDrop = (e) => {
    const id = e.dataTransfer.getData('text');
    // Perform some operation and add attributes
    setAttributes({...attributes, [id]: { some_attribute: "value" }});
  };

  return (
    <div>
      <h1>FlowMaster</h1>
      <div id="dropZone" onDrop={handleDrop} onDragOver={(e) => e.preventDefault()}>
        Drop Zone
      </div>
      <div>
        <div id="element1" draggable="true" onDragStart={(e) => e.dataTransfer.setData('text', 'element1')}>
          Element 1
        </div>
      </div>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
