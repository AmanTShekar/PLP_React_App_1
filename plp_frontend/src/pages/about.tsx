import React from "react";

const About: React.FC = () => {
  return (
    <div className="max-w-3xl mx-auto py-20 text-gray-200">
      <h1 className="text-4xl font-bold mb-6">About PLP Dashboard</h1>
      <p className="text-gray-400 mb-4">
        PLP Dashboard is a modern learning management tool designed to help instructors track student performance,
        provide AI-driven recommendations, and manage learning resources efficiently.
      </p>
      <p className="text-gray-400">
        With a clean and minimalist dark interface, the platform emphasizes readability and actionable insights.
        It supports personalized recommendations based on pending courses and remedial needs.
      </p>
    </div>
  );
};

export default About;
