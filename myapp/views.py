from django.shortcuts import render, get_object_or_404
from .models import *

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_marks(request, student_id, term_id):
    student = get_object_or_404(Student, id=student_id)
    term = get_object_or_404(Term, id=term_id)
    cats = CAT.objects.filter(student=student, term=term)

    context = {
        'student': student,
        'term': term,
        'cats': cats,
    }
    return render(request, 'marks/student_marks.html', context)

def student_progress(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    terms = Term.objects.all().order_by('-year', 'name')
    subjects = Subject.objects.all()
    progress_data = []

    for term in terms:
        term_data = {
            'term': term,
            'subjects': [],
            'term_average': 0,
            'overall_grade': '',
            'position': ''
        }
        
        total_score = 0
        subject_count = 0
        
        for subject in subjects:
            try:
                cat = CAT.objects.get(student=student, term=term, subject=subject)
                subject_data = {
                    'subject': subject,
                    'cat1': cat.cat1,
                    'cat2': cat.cat2,
                    'cat3': cat.cat3,
                    'average': cat.end_term,
                    'grade': cat.letter_grade,
                    'grade_points': cat.grade_points,
                    'position': cat.position
                }
                total_score += cat.end_term
                subject_count += 1
            except CAT.DoesNotExist:
                subject_data = {
                    'subject': subject,
                    'cat1': 'N/A',
                    'cat2': 'N/A',
                    'cat3': 'N/A',
                    'average': 'N/A',
                    'grade': 'N/A',
                    'grade_points': 'N/A',
                    'position': 'N/A'
                }
            
            term_data['subjects'].append(subject_data)
        
        # Calculate term averages if there are subjects
        if subject_count > 0:
            term_data['term_average'] = round(total_score / subject_count, 2)
            # Determine overall grade based on term average
            if term_data['term_average'] >= 80:
                term_data['overall_grade'] = 'A'
                term_data['position'] = 'First Class'
            elif term_data['term_average'] >= 75:
                term_data['overall_grade'] = 'A-'
                term_data['position'] = 'First Class'
            elif term_data['term_average'] >= 70:
                term_data['overall_grade'] = 'B+'
                term_data['position'] = 'First Class'
            elif term_data['term_average'] >= 65:
                term_data['overall_grade'] = 'B'
                term_data['position'] = 'Second Class Upper'
            elif term_data['term_average'] >= 60:
                term_data['overall_grade'] = 'B-'
                term_data['position'] = 'Second Class Upper'
            elif term_data['term_average'] >= 55:
                term_data['overall_grade'] = 'C+'
                term_data['position'] = 'Second Class Lower'
            elif term_data['term_average'] >= 50:
                term_data['overall_grade'] = 'C'
                term_data['position'] = 'Second Class Lower'
            elif term_data['term_average'] >= 40:
                term_data['overall_grade'] = 'D'
                term_data['position'] = 'Pass'
            else:
                term_data['overall_grade'] = 'F'
                term_data['position'] = 'Fail'
        
        progress_data.append(term_data)

    context = {
        'student': student,
        'progress_data': progress_data,
    }
    return render(request, 'marks/student_progress.html', context)