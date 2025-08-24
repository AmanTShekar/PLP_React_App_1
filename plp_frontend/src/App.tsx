import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import { StudentProvider } from "./context/StudentContext";
import Dashboard from "./pages/dashboard";
import Recommendations from "./pages/Recommendations";
import Home from "./pages/Home";
import ResourceDetail from "./pages/ResourceDetail";
import About from "./pages/About";
import Footer from "./components/footer";

const App: React.FC = () => {
  return (
    <StudentProvider>
      <Router>
        <div className="flex flex-col min-h-screen bg-black text-white">
          {/* Navbar */}
          <nav className="navbar">
            <h1 className="text-2xl font-bold">PLP Dashboard</h1>
            <div className="flex space-x-4">
              <Link to="/" className="nav-link">Home</Link>
              <Link to="/dashboard" className="nav-link">Dashboard</Link>
              <Link to="/about" className="nav-link">About</Link>
            </div>
          </nav>

          {/* Page content */}
          <main>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/students/:studentId/recommendations" element={<Recommendations />} />
              <Route path="/resources/:id" element={<ResourceDetail />} />
              <Route path="/about" element={<About />} /> {/* Added About route */}
            </Routes>
          </main>

          {/* Footer */}
          <Footer />
        </div>
      </Router>
    </StudentProvider>
  );
};

export default App;
