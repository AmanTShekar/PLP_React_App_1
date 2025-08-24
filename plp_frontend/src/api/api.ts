import axios from "axios";

// ------------------------
// Axios API setup
// ------------------------
const API_BASE = "http://localhost:8000/api";

// Get student performance
export const getStudentPerformance = (studentId: string) =>
  axios.get(`${API_BASE}/student/${studentId}/performance/`);

// Get all recommendations for a student
export const getRecommendations = (studentId: string) =>
  axios.get(`${API_BASE}/recommendations/${studentId}/`);

// Trigger recommendation generation for a student
export const triggerRecommendation = (studentId: string) =>
  axios.post(`${API_BASE}/recommendations/`, { student_id: studentId });

// Get detailed info for a resource
export const getResourceDetail = (resourceId: string) =>
  axios.get(`${API_BASE}/resources/${resourceId}/`);

// ------------------------
// WebSocket support
// ------------------------
export const createRecommendationSocket = (studentId: string, onMessage: (data: any) => void) => {
  const ws = new WebSocket(`ws://localhost:8000/ws/recommendations/${studentId}/`);

  ws.onopen = () => {
    console.log("WebSocket connected for student:", studentId);
  };

  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    onMessage(data);
  };

  ws.onclose = () => {
    console.log("WebSocket disconnected for student:", studentId);
  };

  ws.onerror = (err) => {
    console.error("WebSocket error:", err);
  };

  return ws;
};
