import React from "react";

interface Props {
  title: string;
  description: string;
  status: "Not Started" | "In Progress" | "Completed";
  onClick?: () => void;
}

const statusColors = {
  "Not Started": "bg-gray-300 text-gray-800",
  "In Progress": "bg-yellow-300 text-yellow-900",
  "Completed": "bg-green-300 text-green-900",
};

const RecommendationCard: React.FC<Props> = ({ title, description, status, onClick }) => {
  return (
    <div
      className="p-4 rounded-xl shadow-lg bg-white/30 backdrop-blur-md cursor-pointer hover:scale-105 transition-transform"
      onClick={onClick}
    >
      <h3 className="text-lg font-semibold">{title}</h3>
      <p className="mt-2 text-gray-700">{description}</p>
      <span
        className={`inline-block mt-3 px-2 py-1 rounded-full text-sm font-medium ${statusColors[status]}`}
      >
        {status}
      </span>
    </div>
  );
};

export default RecommendationCard;
