import axios from 'axios';

const API_BASE = "http://localhost:8000/api";

export const getStudentPerformance = (studentId: string) =>
  axios.get(`${API_BASE}/student/${studentId}/performance/`);

export const getRecommendations = (studentId: string) =>
  axios.get(`${API_BASE}/recommendations/${studentId}/`);

export const triggerRecommendation = (studentId: string) =>
  axios.post(`${API_BASE}/recommendations/`, { student_id: studentId });
