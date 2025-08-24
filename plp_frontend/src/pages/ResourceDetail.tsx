import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import { useStudentContext } from "../context/StudentContext";

interface ResourceDetailData {
  resource_id: string;
  title: string;
  type: string;
  difficulty_level: number;
  course_id: string;
  description?: string;
}

const ResourceDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const { recommendations, updateRecommendationStatus } = useStudentContext();

  const [resource, setResource] = useState<ResourceDetailData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    if (!id) return;
    axios.get(`http://127.0.0.1:8000/api/resources/${id}/`)
      .then(res => setResource(res.data))
      .catch(() => setError("Failed to fetch resource details"))
      .finally(() => setLoading(false));
  }, [id]);

  if (loading) return <div className="text-center mt-10">Loading...</div>;
  if (error) return <div className="text-center text-red-500">{error}</div>;
  if (!resource) return <div className="text-center mt-10">No resource found</div>;

  const rec = recommendations.find(r => r.resource.resource_id === resource.resource_id);

  const handleStatus = (status: Status) => {
    if (!rec) return;
    axios.patch(`http://127.0.0.1:8000/api/recommendations/${rec.id}/`, { status })
      .then(res => updateRecommendationStatus(rec.id, res.data.status))
      .catch(() => alert("Failed to update status"));
  };

  return (
    <div className="max-w-3xl mx-auto p-6 bg-gray-100 rounded-xl shadow-lg">
      <h2 className="text-2xl font-semibold mb-2 text-gray-800">{resource.title}</h2>
      <p className="mb-2 text-gray-700"><strong>Type:</strong> {resource.type}</p>
      <p className="mb-2 text-gray-700"><strong>Difficulty:</strong> {resource.difficulty_level}</p>
      <p className="mb-2 text-gray-700"><strong>Course ID:</strong> {resource.course_id}</p>
      {resource.description && <p className="mb-4 text-gray-600">{resource.description}</p>}

      {rec && (
        <div className="flex items-center space-x-3 mt-4">
          <span className={`px-3 py-1 rounded text-white ${
            rec.status === "Completed" ? "bg-green-600" :
            rec.status === "In Progress" ? "bg-yellow-500" : "bg-gray-500"
          }`}>{rec.status}</span>

          <button onClick={() => handleStatus("In Progress")} className="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600">Start</button>
          <button onClick={() => handleStatus("Completed")} className="px-3 py-1 bg-green-500 text-white rounded hover:bg-green-600">Complete</button>
        </div>
      )}
    </div>
  );
};

export default ResourceDetail;
