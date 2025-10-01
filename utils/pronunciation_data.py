"""Pronunciation guide data access layer"""

from data.pronunciation_phrases import PRONUNCIATION_PHRASES

class PronunciationData:
    """Class to access and manage pronunciation guide data"""
    
    def __init__(self):
        self.data = PRONUNCIATION_PHRASES
    
    def get_categories(self):
        """Get all pronunciation categories with metadata"""
        categories = []
        for category_id, category_data in self.data.items():
            categories.append({
                'id': category_id,
                'name': category_id,
                'category': category_data['category'],
                'difficulty': category_data['difficulty'],
                'phrase_count': len(category_data['phrases']),
                'description': f"Practice {len(category_data['phrases'])} essential phrases for {category_data['category']}"
            })
        return categories
    
    def get_category_by_id(self, category_id):
        """Get a specific pronunciation category by ID"""
        category_data = self.data.get(category_id)
        if category_data:
            return {
                'id': category_id,
                'name': category_id,
                'category': category_data['category'],
                'difficulty': category_data['difficulty'],
                'description': f"Practice {len(category_data['phrases'])} essential phrases for {category_data['category']}",
                'phrases': category_data['phrases'],
                'tips': self._extract_tips(category_data),
                'challenges': self._extract_challenges(category_data),
                'minimal_pairs': self._extract_minimal_pairs(category_data)
            }
        return None
    
    def get_categories_by_difficulty(self, difficulty):
        """Get categories filtered by difficulty level"""
        categories = []
        for category_id, category_data in self.data.items():
            if category_data['difficulty'] == difficulty:
                categories.append({
                    'id': category_id,
                    'name': category_id,
                    'category': category_data['category'],
                    'difficulty': category_data['difficulty']
                })
        return categories
    
    def get_all_phrases(self):
        """Get all phrases across all categories"""
        all_phrases = []
        for category_id, category_data in self.data.items():
            for phrase_data in category_data['phrases']:
                all_phrases.append({
                    'category': category_id,
                    **phrase_data
                })
        return all_phrases
    
    def search_phrase(self, search_term):
        """Search for phrases containing the search term"""
        results = []
        search_lower = search_term.lower()
        
        for category_id, category_data in self.data.items():
            for phrase_data in category_data['phrases']:
                if search_lower in phrase_data['phrase'].lower():
                    results.append({
                        'category': category_id,
                        **phrase_data
                    })
        
        return results
    
    def get_difficulties(self):
        """Get list of unique difficulty levels"""
        difficulties = set()
        for category_data in self.data.values():
            difficulties.add(category_data['difficulty'])
        return sorted(list(difficulties))
    
    def _extract_tips(self, category_data):
        """Extract pronunciation tips from phrases"""
        tips = []
        for phrase_data in category_data['phrases']:
            if 'tips' in phrase_data and phrase_data['tips']:
                tips.append(phrase_data['tips'])
        
        # Add general tips if available
        if not tips:
            tips = [
                'Pay attention to word stress patterns',
                'Practice speaking slowly at first',
                'Record yourself and compare with the audio',
                'Focus on difficult sounds individually'
            ]
        
        return tips[:5]  # Return up to 5 tips
    
    def _extract_challenges(self, category_data):
        """Extract common pronunciation challenges"""
        # This would be enhanced with actual challenge data
        return []
    
    def _extract_minimal_pairs(self, category_data):
        """Extract minimal pairs for sound discrimination practice"""
        # This would be enhanced with actual minimal pair data
        return []
