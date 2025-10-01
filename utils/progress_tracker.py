"""Track user progress across all learning modules with database persistence"""

import streamlit as st
from datetime import datetime
from utils.database import get_session, User, Progress

class ProgressTracker:
    """Track user progress across all learning modules"""

    def __init__(self, user_name=None):
        self.user_name = user_name or st.session_state.get('user_name', '')
        self.load_progress()

    def load_progress(self):
        """Load progress from database or initialize new progress"""
        if not self.user_name:
            # Initialize empty progress for anonymous users
            self._init_empty_progress()
            return

        try:
            session = get_session()

            # Get or create user
            user = session.query(User).filter_by(name=self.user_name).first()
            if not user:
                user = User(name=self.user_name)
                session.add(user)
                session.commit()

            # Get or create progress
            progress = session.query(Progress).filter_by(user_name=self.user_name).first()
            if not progress:
                progress = Progress(
                    user_name=self.user_name,
                    vocabulary_by_category={},
                    mastered_words=[],
                    conversation_scenarios={},
                    grammar_by_topic={},
                    reading_by_type={},
                    reading_scores=[],
                    pronunciation_by_category={},
                    writing_by_type={},
                    achievements=[],
                    activity_history=[]
                )
                session.add(progress)
                session.commit()

            # Load into session state
            st.session_state.progress_data = {
                'vocabulary': {
                    'words_learned': progress.vocabulary_words_learned or 0,
                    'by_category': progress.vocabulary_by_category or {},
                    'mastered_words': progress.mastered_words or [],
                    'completion_rate': 0
                },
                'conversations': {
                    'completed': progress.conversations_completed or 0,
                    'scenarios': progress.conversation_scenarios or {},
                    'completion_rate': 0
                },
                'grammar': {
                    'completed': progress.grammar_completed or 0,
                    'by_topic': progress.grammar_by_topic or {},
                    'accuracy': self._calculate_grammar_accuracy(progress.grammar_by_topic or {}),
                    'completion_rate': 0
                },
                'reading': {
                    'completed': progress.reading_completed or 0,
                    'by_type': progress.reading_by_type or {},
                    'comprehension_scores': progress.reading_scores or [],
                    'completion_rate': 0
                },
                'pronunciation': {
                    'practiced': progress.pronunciation_practiced or 0,
                    'by_category': progress.pronunciation_by_category or {},
                    'completion_rate': 0
                },
                'writing': {
                    'completed': progress.writing_completed or 0,
                    'by_type': progress.writing_by_type or {},
                    'avg_score': self._calculate_writing_avg(progress.writing_by_type or {}),
                    'completion_rate': 0
                },
                'achievements': progress.achievements or [],
                'activity_history': progress.activity_history or [],
                'last_updated': str(progress.last_updated) if progress.last_updated else str(datetime.now())
            }

            session.close()

        except Exception as e:
            st.error(f"Error loading progress: {str(e)}")
            self._init_empty_progress()

    def _init_empty_progress(self):
        """Initialize empty progress structure"""
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

    def _save_to_database(self):
        """Save current progress to database"""
        if not self.user_name:
            return

        try:
            session = get_session()
            progress = session.query(Progress).filter_by(user_name=self.user_name).first()

            if progress:
                data = st.session_state.progress_data
                progress.vocabulary_words_learned = data['vocabulary']['words_learned']
                progress.vocabulary_by_category = data['vocabulary']['by_category']
                progress.mastered_words = data['vocabulary']['mastered_words']
                progress.conversations_completed = data['conversations']['completed']
                progress.conversation_scenarios = data['conversations']['scenarios']
                progress.grammar_completed = data['grammar']['completed']
                progress.grammar_by_topic = data['grammar']['by_topic']
                progress.reading_completed = data['reading']['completed']
                progress.reading_by_type = data['reading']['by_type']
                progress.reading_scores = data['reading']['comprehension_scores']
                progress.pronunciation_practiced = data['pronunciation']['practiced']
                progress.pronunciation_by_category = data['pronunciation']['by_category']
                progress.writing_completed = data['writing']['completed']
                progress.writing_by_type = data['writing']['by_type']
                progress.achievements = data['achievements']
                progress.activity_history = data['activity_history']
                progress.last_updated = datetime.now()

                session.commit()

            session.close()
        except Exception as e:
            st.error(f"Error saving progress: {str(e)}")

    def _calculate_grammar_accuracy(self, by_topic):
        """Calculate overall grammar accuracy from topic data"""
        total_correct = sum(t.get('correct', 0) for t in by_topic.values())
        total_questions = sum(t.get('total', 0) for t in by_topic.values())
        return (total_correct / total_questions * 100) if total_questions > 0 else 0

    def _calculate_writing_avg(self, by_type):
        """Calculate average writing score"""
        total_score = sum(t.get('total_score', 0) for t in by_type.values())
        total_exercises = sum(t.get('completed', 0) for t in by_type.values())
        return (total_score / total_exercises) if total_exercises > 0 else 0

    def add_vocabulary(self, category, word):
        """Add learned vocabulary word"""
        progress = st.session_state.progress_data['vocabulary']

        # Update category count
        if category not in progress['by_category']:
            progress['by_category'][category] = 0

        # Add word if not already mastered
        if word not in progress['mastered_words']:
            progress['mastered_words'].append(word)
            progress['words_learned'] = len(progress['mastered_words'])
            progress['by_category'][category] = progress['by_category'].get(category, 0) + 1

        self._update_timestamp()
        self._check_achievements('vocabulary', progress['words_learned'])
        self._save_to_database()

    def get_vocabulary_progress(self, category):
        """Get vocabulary progress for a specific category"""
        progress = st.session_state.progress_data['vocabulary']
        mastered_words = progress.get('mastered_words', [])

        # Filter words by category
        from utils.vocabulary_data import VocabularyData
        vocab_data = VocabularyData()
        category_words = vocab_data.get_words_by_category(category)
        category_word_list = [w['word'] for w in category_words]

        learned_in_category = [w for w in mastered_words if w in category_word_list]

        return {
            'learned': learned_in_category,
            'total': len(category_word_list)
        }

    def add_conversation(self, scenario_id):
        """Mark conversation scenario as completed"""
        progress = st.session_state.progress_data['conversations']

        if scenario_id not in progress['scenarios']:
            progress['scenarios'][scenario_id] = {'completed': False, 'attempts': 0}

        progress['scenarios'][scenario_id]['attempts'] += 1

        if not progress['scenarios'][scenario_id]['completed']:
            progress['scenarios'][scenario_id]['completed'] = True
            progress['completed'] += 1

        self._update_timestamp()
        self._check_achievements('conversations', progress['completed'])
        self._save_to_database()

    def add_grammar_exercise(self, topic):
        """Add completed grammar exercise"""
        progress = st.session_state.progress_data['grammar']

        if topic not in progress['by_topic']:
            progress['by_topic'][topic] = 0

        progress['by_topic'][topic] += 1
        progress['completed'] += 1

        self._update_timestamp()
        self._check_achievements('grammar', progress['completed'])
        self._save_to_database()

    def add_reading_exercise(self, passage_id):
        """Add completed reading exercise"""
        progress = st.session_state.progress_data['reading']
        progress['completed'] += 1

        self._update_timestamp()
        self._check_achievements('reading', progress['completed'])
        self._save_to_database()

    def add_writing_exercise(self, exercise_id):
        """Add completed writing exercise"""
        progress = st.session_state.progress_data['writing']
        progress['completed'] += 1

        self._update_timestamp()
        self._check_achievements('writing', progress['completed'])
        self._save_to_database()

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
        activity = st.session_state.progress_data.get('activity_history', [])
        if activity:
            return [item.get('count', 0) for item in activity[-days:]]
        return []

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

        st.session_state.progress_data['activity_history'] = activity_history[-30:]

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
                    # Check if already earned
                    already_earned = any(
                        a.get('title') == title for a in achievements
                    )
                    if not already_earned:
                        achievements.append(achievement)
                        st.session_state.progress_data['achievements'] = achievements
                        st.balloons()

    def complete_lesson(self, lesson_name):
        """Mark a lesson as completed"""
        if lesson_name not in self.progress['lessons']['completed']:
            self.progress['lessons']['completed'].append(lesson_name)
            self.progress['lessons']['total_lessons'] = len(self.progress['lessons']['completed'])
            self.save_progress()

    def get_lesson_progress(self):
        """Get completed lessons"""
        return self.progress['lessons']['completed']

    def get_recent_achievements(self):
        """Get recent achievements"""
        # This would typically query a database
        # For now, return mock achievements
        achievements = []

        if self.progress['vocabulary']['words_learned'] >= 10:
            achievements.append({
                'title': 'Vocabulary Master',
                'description': 'Learned 10+ new words!'
            })

        if self.progress['conversations']['completed'] >= 3:
            achievements.append({
                'title': 'Conversation Expert',
                'description': 'Completed 3+ conversations!'
            })

        if self.progress['lessons']['total_lessons'] >= 1:
            achievements.append({
                'title': 'Lesson Starter',
                'description': 'Completed your first lesson!'
            })

        return achievements[-3:]  # Return last 3 achievements