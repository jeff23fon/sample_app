// ...existing code...
import React, { useEffect, useState } from "react";
import ReactDOM from "react-dom/client";

const App: React.FC = () => {
    const [data, setData] = useState<string>("Loading...");

    useEffect(() => {
        fetch("/api/hello")
            .then((res) => res.json())
            .then((j) => setData(j.message))
            .catch(() => setData("Error fetching data"));
    }, []);

    return (
        <div>
            <pre>{data}</pre>
        </div>
    );
};

const root = ReactDOM.createRoot(document.getElementById("root") as HTMLElement);
root.render(<App />);
// ...existing code...