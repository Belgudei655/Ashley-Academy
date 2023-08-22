document.addEventListener('DOMContentLoaded', function() {
    if (window.location.pathname === '/website/courses') {
        fetch('get_json_courses/')  
            .then(response => response.json())
            .then(jsonData => {
                const coursesContainer = document.getElementById('coursesContainer');
                
                jsonData.forEach(course => {
                    const courseDiv = document.createElement('div');
                    courseDiv.className = 'coursesContent';
                    
                    const courseLink = document.createElement('a');
                    courseLink.className = 'fullSubjectDisplay';
                    courseLink.textContent = course.name;
                    courseDiv.appendChild(courseLink);
                    
                    course.subjects.forEach(subject => {
                        const subjectLink = document.createElement('a');
                        subjectLink.className = 'specificCourses';
                        subjectLink.textContent = subject.name;
                        
                        subjectLink.href = '/website/disCourses/' + encodeURIComponent(subject.name);
                        courseDiv.appendChild(subjectLink);
                    });
                    
                    coursesContainer.appendChild(courseDiv);
                });
            })
            .catch(error => {
                console.error('Error fetching JSON data:', error);
            });
    }
});
