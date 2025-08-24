import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { CircularProgressbar, buildStyles } from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";
import { useStudentContext } from "../context/StudentContext";

const Dashboard: React.FC = () => {
  const { students, setStudents } = useStudentContext();
  const navigate = useNavigate();

  useEffect(() => {
    fetch("/api/students/")
      .then(res => res.json())
      .then(data => setStudents(data.results || data))
      .catch(err => console.error(err));
  }, [setStudents]);

  if (!students.length)
    return <div className="empty-state">No students found</div>;

  return (
    <div className="px-4 py-8">
      <h1 className="text-4xl font-bold mb-8 text-center text-white">Hi, Instructor!</h1>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8 justify-items-center">
        {students.map(student => {
          const totalCourses = student.completed_courses.length + student.pending_courses.length;
          const progress = totalCourses ? (student.completed_courses.length / totalCourses) * 100 : 0;
          const remedialSubjects = student.subject_scores
            .filter((s: any) => s.remedial_needed)
            .map((s: any) => s.subject);
          const hasRemedial = remedialSubjects.length > 0;

          return (
            <div
              key={student.student_id}
              className={`frosted-card max-w-sm w-full border transition transform hover:scale-105 hover:shadow-2xl cursor-pointer 
                ${hasRemedial ? "border-red-500" : "border-gray-600"}`}
              onClick={() => navigate(`/students/${student.student_id}/recommendations`)}
            >
              <h2 className="text-2xl font-bold mb-4 text-white">{student.name}</h2>

              {hasRemedial && (
                <div className="mb-4 px-4 py-1 bg-red-600 text-white font-semibold rounded-full text-center">
                  Remedial Needed
                </div>
              )}

              <div className="progress-container mb-4">
                <CircularProgressbar
                  value={progress}
                  text={`${Math.round(progress)}%`}
                  styles={buildStyles({
                    textSize: "24px",
                    pathColor: "#4ade80",
                    textColor: "#ffffff",
                    trailColor: "#374151",
                  })}
                />
              </div>

              <p className="text-center text-gray-300 font-medium mt-2">
                Completed: {student.completed_courses.length} / {totalCourses} courses
              </p>

              {hasRemedial && (
                <div className="mt-3 text-center text-red-400 font-medium">
                  <p>Subjects needing remedial:</p>
                  <ul className="list-disc list-inside">
                    {remedialSubjects.map(sub => (
                      <li key={sub}>{sub}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default Dashboard;
