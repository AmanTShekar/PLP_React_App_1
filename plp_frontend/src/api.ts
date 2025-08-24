import axios from "axios";

const API_BASE = "http://127.0.0.1:8000/api";

// Fetch a single student's performance & courses
export const getStudentPerformance = (studentId: string) =>
  axios.get(`${API_BASE}/students/${studentId}/performance/`);

// Fetch recommendations filtered for the student
export const getRecommendations = (studentId: string) =>
  axios.get(`${API_BASE}/students/${studentId}/recommendations/`);

// Trigger AI to generate recommendations
export const triggerRecommendation = (studentId: string) =>
  axios.post(`${API_BASE}/recommendations/`, { student_id: studentId });

// Fetch a specific resource
export const getResourceDetail = (resourceId: string) =>
  axios.get(`${API_BASE}/resources/${resourceId}/`);

// Fetch all students
export const getAllStudents = () =>
  axios.get(`${API_BASE}/students/`);

// Fetch all resources
export const getAllResources = () =>
  axios.get(`${API_BASE}/resources/`);
