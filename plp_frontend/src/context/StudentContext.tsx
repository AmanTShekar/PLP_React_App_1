import React, { createContext, useContext, useState, ReactNode } from "react";

export type Status = "Not Started" | "In Progress" | "Completed";

export interface Resource {
  resource_id: string;
  title: string;
  type: string;
}

export interface Recommendation {
  id: number;
  status: Status;
  resource: Resource;
  student_id: string;
}

export interface Student {
  student_id: string;
  name: string;
  email: string;
  performance_score: number;
  completed_courses: string[];
  pending_courses: string[];
  remedial_needed: boolean;
}

interface StudentContextType {
  students: Student[];
  setStudents: React.Dispatch<React.SetStateAction<Student[]>>;
  recommendations: Recommendation[];
  setRecommendations: React.Dispatch<React.SetStateAction<Recommendation[]>>;
  updateRecommendationStatus: (id: number, status: Status) => void;
}

const StudentContext = createContext<StudentContextType | undefined>(undefined);

export const StudentProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [students, setStudents] = useState<Student[]>([]);
  const [recommendations, setRecommendations] = useState<Recommendation[]>([]);

  const updateRecommendationStatus = (id: number, status: Status) => {
    setRecommendations((prev) =>
      prev.map((r) => (r.id === id ? { ...r, status } : r))
    );
  };

  return (
    <StudentContext.Provider
      value={{ students, setStudents, recommendations, setRecommendations, updateRecommendationStatus }}
    >
      {children}
    </StudentContext.Provider>
  );
};

export const useStudentContext = (): StudentContextType => {
  const context = useContext(StudentContext);
  if (!context) throw new Error("useStudentContext must be used within StudentProvider");
  return context;
};
