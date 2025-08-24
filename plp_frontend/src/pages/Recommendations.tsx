import React, { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { useStudentContext } from "../context/StudentContext";
import { getRecommendations } from "../api";

const Recommendations: React.FC = () => {
  const { studentId } = useParams<{ studentId: string }>();
  const { recommendations, setRecommendations, updateRecommendationStatus } = useStudentContext();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!studentId) return;
    getRecommendations(studentId)
      .then(res => setRecommendations(res.data.results || res.data))
      .finally(() => setLoading(false));
  }, [studentId, setRecommendations]);

  const handleStatusChange = (recId: number, newStatus: Status) => {
    updateRecommendationStatus(recId, newStatus);
  };

  if (loading)
    return <div className="text-center mt-10 text-gray-300">Loading recommendations...</div>;

  if (!recommendations.length)
    return <div className="text-center mt-10 text-gray-300">No recommendations found</div>;

  return (
    <div className="px-6 py-8">
      <h1 className="text-3xl font-bold mb-6 text-center text-gray-200">Your Recommendations</h1>
      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 justify-items-center">
        {recommendations.map((rec) => (
          <div
            key={rec.id}
            className="w-80 p-6 bg-gray-800 text-gray-100 rounded-xl shadow-lg transform hover:scale-105 transition-transform duration-300"
          >
            <h2 className="text-xl font-semibold mb-2">{rec.resource.title}</h2>
            <p className="mb-2 text-sm text-gray-300">Type: {rec.resource.type}</p>

            <div
              className={`inline-block px-3 py-1 rounded text-white mb-4 ${
                rec.status === "Completed"
                  ? "bg-green-600"
                  : rec.status === "In Progress"
                  ? "bg-yellow-500 text-gray-900"
                  : "bg-gray-600"
              }`}
            >
              {rec.status}
            </div>

            <div className="flex flex-wrap gap-2 mt-2">
              <button
                onClick={() => handleStatusChange(rec.id, "In Progress")}
                className="px-3 py-1 bg-blue-600 text-white rounded hover:bg-blue-700 transition"
              >
                Start
              </button>
              <button
                onClick={() => handleStatusChange(rec.id, "Completed")}
                className="px-3 py-1 bg-green-600 text-white rounded hover:bg-green-700 transition"
              >
                Complete
              </button>
              <Link
                to={`/resources/${rec.resource.resource_id}`}
                className="px-3 py-1 bg-purple-600 text-white rounded hover:bg-purple-700 transition"
              >
                View Resource
              </Link>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Recommendations;
