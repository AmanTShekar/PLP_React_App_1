import React from "react";
import { Link } from "react-router-dom";

const Home: React.FC = () => {
  return (
    <div className="text-center py-20">
      <h1 className="text-5xl font-bold mb-6 text-gray-100">Welcome to PLP Dashboard</h1>
      <p className="text-gray-400 mb-8">
        Track student performance, manage recommendations, and assign learning resources easily.
      </p>
      <Link
        to="/dashboard"
        className="px-6 py-3 bg-purple-600 text-white rounded-xl hover:bg-purple-700 transition font-semibold"
      >
        Go to Dashboard
      </Link>
    </div>
  );
};

export default Home;
