import streamlit as st
import json
from datetime import datetime, timedelta
import os

class ProgressTracker:
    """Track user progress across all learning modules"""
    
    def __init__(self):
        self.data_file = 'user_progress.json'
        self.load_progress()
    
    def load_progress(self):
        """Load progress from session state or initialize new progress"""
        if 'progress_data' not in st.session_state:
            st.session_state.progress_data = {
                'vocabulary': {
                    'words_learned': 0,
                    'by_category': {},
                    'mastered_words': [],
                    'completion_rate': 0
                },
                'conversations': {
                    'completed': 0,
                    'scenarios': {},
                    'completion_rate': 0
                },
                'grammar': {
                    'completed': 0,
                    'by_topic': {},
                    'accuracy': 0,
                    'completion_rate': 0
                },
                'reading': {
                    'completed': 0,
                    'by_type': {},
                    'comprehension_scores': [],
                    'completion_rate': 0
                },
                'pronunciation': {
                    'practiced': 0,
                    'by_category': {},
                    'completion_rate': 0
                },
                'writing': {
                    'completed': 0,
                    'by_type': {},
                    'avg_score': 0,
                    'completion_rate': 0
                },
                'achievements': [],
                'activity_history': [],
                'last_updated': str(datetime.now())
            }
    
    def update_vocabulary_progress(self, word, category, mastered=False):
        """Update vocabulary learning progress"""
        progress = st.session_state.progress_data['vocabulary']
        
        # Update category count
        if category not in progress['by_category']:
            progress['by_category'][category] = 0
        progress['by_category'][category] += 1
        
        # Update mastered words
        if mastered and word not in progress['mastered_words']:
            progress['mastered_words'].append(word)
            progress['words_learned'] = len(progress['mastered_words'])
        
        self._update_timestamp()
        self._check_achievements('vocabulary', progress['words_learned'])
    
    def update_conversation_progress(self, scenario_id, completed=True):
        """Update conversation practice progress"""
        progress = st.session_state.progress_data['conversations']
        
        if scenario_id not in progress['scenarios']:
            progress['scenarios'][scenario_id] = {'completed': False, 'attempts': 0}
        
        progress['scenarios'][scenario_id]['attempts'] += 1
        
        if completed and not progress['scenarios'][scenario_id]['completed']:
            progress['scenarios'][scenario_id]['completed'] = True
            progress['completed'] += 1
        
        self._update_timestamp()
        self._check_achievements('conversations', progress['completed'])
    
    def update_grammar_progress(self, topic, correct, total):
        """Update grammar exercise progress"""
        progress = st.session_state.progress_data['grammar']
        
        if topic not in progress['by_topic']:
            progress['by_topic'][topic] = {'completed': 0, 'correct': 0, 'total': 0}
        
        progress['by_topic'][topic]['completed'] += 1
        progress['by_topic'][topic]['correct'] += correct
        progress['by_topic'][topic]['total'] += total
        progress['completed'] += 1
        
        # Calculate overall accuracy
        total_correct = sum(t['correct'] for t in progress['by_topic'].values())
        total_questions = sum(t['total'] for t in progress['by_topic'].values())
        progress['accuracy'] = (total_correct / total_questions * 100) if total_questions > 0 else 0
        
        self._update_timestamp()
        self._check_achievements('grammar', progress['completed'])
    
    def update_reading_progress(self, content_type, score):
        """Update reading comprehension progress"""
        progress = st.session_state.progress_data['reading']
        
        if content_type not in progress['by_type']:
            progress['by_type'][content_type] = 0
        progress['by_type'][content_type] += 1
        progress['completed'] += 1
        progress['comprehension_scores'].append(score)
        
        self._update_timestamp()
        self._check_achievements('reading', progress['completed'])
    
    def update_pronunciation_progress(self, phrase, category):
        """Update pronunciation practice progress"""
        progress = st.session_state.progress_data['pronunciation']
        
        if category not in progress['by_category']:
            progress['by_category'][category] = 0
        progress['by_category'][category] += 1
        progress['practiced'] += 1
        
        self._update_timestamp()
        self._check_achievements('pronunciation', progress['practiced'])
    
    def update_writing_progress(self, exercise_type, score):
        """Update writing exercise progress"""
        progress = st.session_state.progress_data['writing']
        
        if exercise_type not in progress['by_type']:
            progress['by_type'][exercise_type] = {'completed': 0, 'total_score': 0}
        
        progress['by_type'][exercise_type]['completed'] += 1
        progress['by_type'][exercise_type]['total_score'] += score
        progress['completed'] += 1
        
        # Calculate average score
        total_score = sum(t['total_score'] for t in progress['by_type'].values())
        total_exercises = sum(t['completed'] for t in progress['by_type'].values())
        progress['avg_score'] = (total_score / total_exercises) if total_exercises > 0 else 0
        
        self._update_timestamp()
        self._check_achievements('writing', progress['completed'])
    
    def get_overall_progress(self):
        """Get overall progress across all modules"""
        progress = st.session_state.progress_data
        
        # Calculate completion rates (assuming 100 items per module as target)
        progress['vocabulary']['completion_rate'] = min(progress['vocabulary']['words_learned'], 100)
        progress['conversations']['completion_rate'] = min(progress['conversations']['completed'] * 10, 100)
        progress['grammar']['completion_rate'] = min(progress['grammar']['completed'] * 5, 100)
        progress['reading']['completion_rate'] = min(progress['reading']['completed'] * 10, 100)
        progress['pronunciation']['completion_rate'] = min(progress['pronunciation']['practiced'] * 2, 100)
        progress['writing']['completion_rate'] = min(progress['writing']['completed'] * 10, 100)
        
        return progress
    
    def get_activity_history(self, days=7):
        """Get activity history for the last N days"""
        return st.session_state.progress_data.get('activity_history', [])[-days:]
    
    def get_recent_achievements(self, limit=5):
        """Get recent achievements"""
        achievements = st.session_state.progress_data.get('achievements', [])
        return sorted(achievements, key=lambda x: x.get('date', ''), reverse=True)[:limit]
    
    def _update_timestamp(self):
        """Update last activity timestamp"""
        st.session_state.progress_data['last_updated'] = str(datetime.now())
        
        # Add to activity history
        activity_history = st.session_state.progress_data.get('activity_history', [])
        today = datetime.now().date()
        
        if not activity_history or activity_history[-1].get('date') != str(today):
            activity_history.append({'date': str(today), 'count': 1})
        else:
            activity_history[-1]['count'] += 1
        
        st.session_state.progress_data['activity_history'] = activity_history[-30:]  # Keep last 30 days
    
    def _check_achievements(self, module, count):
        """Check and award achievements"""
        achievements = st.session_state.progress_data.get('achievements', [])
        
        achievement_milestones = {
            'vocabulary': [
                (10, "First 10 Words", "Learned your first 10 vocabulary words!"),
                (50, "Vocabulary Builder", "Mastered 50 vocabulary words!"),
                (100, "Word Master", "Incredible! 100 words learned!"),
            ],
            'conversations': [
                (5, "Conversationalist", "Completed 5 conversation scenarios!"),
                (10, "Dialogue Expert", "Mastered 10 conversation scenarios!"),
            ],
            'grammar': [
                (10, "Grammar Rookie", "Completed 10 grammar exercises!"),
                (25, "Grammar Pro", "Completed 25 grammar exercises!"),
                (50, "Grammar Master", "Outstanding! 50 grammar exercises completed!"),
            ],
            'reading': [
                (5, "Avid Reader", "Read and comprehended 5 articles!"),
                (10, "Reading Champion", "Completed 10 reading exercises!"),
            ],
            'pronunciation': [
                (20, "Pronunciation Practitioner", "Practiced 20 phrases!"),
                (50, "Speaking Star", "Practiced 50 phrases!"),
            ],
            'writing': [
                (5, "Writing Beginner", "Completed 5 writing exercises!"),
                (10, "Skilled Writer", "Completed 10 writing exercises!"),
            ]
        }
        
        if module in achievement_milestones:
            for milestone, title, description in achievement_milestones[module]:
                if count == milestone:
                    achievement = {
                        'title': title,
                        'description': description,
                        'date': str(datetime.now()),
                        'module': module
                    }
                    if achievement not in achievements:
                        achievements.append(achievement)
                        st.session_state.progress_data['achievements'] = achievements
