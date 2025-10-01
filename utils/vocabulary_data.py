"""Vocabulary data access layer"""

from data.vocabulary_data import VOCABULARY_DATA, get_all_categories as get_cats

class VocabularyData:
    """Class to access and manage vocabulary data"""
    
    def __init__(self):
        self.data = VOCABULARY_DATA
    
    def get_categories(self):
        """Get all vocabulary categories with metadata"""
        categories = []
        for category_name in get_cats():
            categories.append({
                'name': category_name,
                'word_count': len(self.data[category_name])
            })
        return categories
    
    def get_words_by_category(self, category):
        """Get all words for a specific category"""
        return self.data.get(category, [])
    
    def get_category_names(self):
        """Get list of category names"""
        return get_cats()
    
    def get_total_words(self):
        """Get total number of vocabulary words"""
        return sum(len(words) for words in self.data.values())
    
    def search_word(self, search_term):
        """Search for a word across all categories"""
        results = []
        search_lower = search_term.lower()
        
        for category, words in self.data.items():
            for word_data in words:
                if search_lower in word_data['word'].lower() or search_lower in word_data['definition'].lower():
                    results.append({
                        'category': category,
                        **word_data
                    })
        
        return results
