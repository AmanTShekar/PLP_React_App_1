from django.core.management.base import BaseCommand
from learning.models import Student, LearningResource, Recommendation, SubjectScore

class Command(BaseCommand):
    help = "Seed students, learning resources, AI-driven recommendations, and remedials"

    def handle(self, *args, **kwargs):
        # -------------------
        # Clear existing data
        # -------------------
        Recommendation.objects.all().delete()
        LearningResource.objects.all().delete()
        SubjectScore.objects.all().delete()
        Student.objects.all().delete()
        self.stdout.write(self.style.WARNING("Cleared all previous data."))

        # -------------------
        # Students
        # -------------------
        students_data = [
            {"student_id": "S1", "name": "Alex Doe", "email": "s1@example.com", "performance_score": 58.0, "completed_courses": ["CS101"], "pending_courses": ["CS102", "CS201"]},
            {"student_id": "S2", "name": "Jane Smith", "email": "s2@example.com", "performance_score": 72.0, "completed_courses": ["CS101", "CS102"], "pending_courses": ["CS201"]},
            {"student_id": "S3", "name": "Bob Lee", "email": "s3@example.com", "performance_score": 90.0, "completed_courses": ["CS101", "CS102", "CS201"], "pending_courses": []},
            {"student_id": "S4", "name": "Charlie Brown", "email": "s4@example.com", "performance_score": 45.0, "completed_courses": ["CS101"], "pending_courses": ["CS102"]},
            {"student_id": "S5", "name": "Diana Prince", "email": "s5@example.com", "performance_score": 65.0, "completed_courses": ["CS101", "CS102"], "pending_courses": ["CS201"]},
        ]

        students = []
        for s in students_data:
            student = Student.objects.create(
                student_id=s["student_id"],
                name=s["name"],
                email=s["email"],
                performance_score=s["performance_score"],
                completed_courses=s["completed_courses"],
                pending_courses=s["pending_courses"],
                remedial_needed=s["performance_score"] < 60
            )
            # Optionally, create subject scores
            for course in s["completed_courses"] + s["pending_courses"]:
                score = s["performance_score"]  # example score
                SubjectScore.objects.create(student=student, subject=course, score=score, remedial_needed=score < 60)
            students.append(student)

        self.stdout.write(self.style.SUCCESS(f"{len(students)} students created."))

        # -------------------
        # Learning Resources
        # -------------------
        resources_data = [
            {"resource_id": "R1", "title": "Arrays 101", "type": "tutorial", "difficulty_level": 1, "course_id": "CS102", "recommendation_priority": 9},
            {"resource_id": "R2", "title": "Pointers Deep Dive", "type": "article", "difficulty_level": 3, "course_id": "CS201", "recommendation_priority": 6},
            {"resource_id": "R3", "title": "Recursion Explained", "type": "video", "difficulty_level": 2, "course_id": "CS201", "recommendation_priority": 7},
            {"resource_id": "R4", "title": "Data Structures Crash", "type": "video", "difficulty_level": 1, "course_id": "CS102", "recommendation_priority": 10},
            # Remedial resources
            {"resource_id": "RM1", "title": "Remedial: CS Basics", "type": "tutorial", "difficulty_level": 1, "course_id": "CS101", "recommendation_priority": 1},
            {"resource_id": "RM2", "title": "Remedial: Algorithms", "type": "video", "difficulty_level": 1, "course_id": "CS102", "recommendation_priority": 2},
        ]

        resources = []
        for r in resources_data:
            res = LearningResource.objects.create(
                resource_id=r["resource_id"],
                title=r["title"],
                type=r["type"],
                difficulty_level=r["difficulty_level"],
                course_id=r["course_id"],
                recommendation_priority=r["recommendation_priority"],
            )
            resources.append(res)

        self.stdout.write(self.style.SUCCESS(f"{len(resources)} resources created."))

        # -------------------
        # Recommendations
        # -------------------
        rec_count = 0
        for student in students:
            for resource in resources:
                # Assign remedial resources if student needs remedial
                if student.remedial_needed and resource.resource_id.startswith("RM"):
                    rec, created = Recommendation.objects.get_or_create(student=student, resource=resource, defaults={"status": "Not Started"})
                    if created:
                        rec_count += 1
                # Assign normal resources if course is pending
                elif resource.course_id in student.pending_courses and not resource.resource_id.startswith("RM"):
                    rec, created = Recommendation.objects.get_or_create(student=student, resource=resource, defaults={"status": "Not Started"})
                    if created:
                        rec_count += 1

        self.stdout.write(self.style.SUCCESS(f"{rec_count} recommendations created."))
        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
