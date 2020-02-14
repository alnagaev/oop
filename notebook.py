import datetime

last_id = 0

class Note:
    """Соответствует заметки в ежедневнике.
     Допускает поиск по строке и хранит тэги для каждой заметки"""

     
    def __init__(self, memo, tags = ''):
         """Создает заметку с памяткой и опциональными тэгами разделенными запятой
         Автоматически устанавливает дату создания
         """

         self.memo = memo
         self.tags = tags
         self.creation_day = datetime.date.today()
         global last_id
         last_id +=1
         self.id = last_id


    # def __str__(self):
    #     pass

    
    # def __repr__(self):
    #     pass


    def match(self, filter):
        """Определяет соответствие заметки по ключевому запросу
        Возвращает True или False в зависимости от результата.
        Метод чувствителен к регистру и поиск проходит как по заметке так и по тэгам
        """

        return filter in self.memo or filter in self.tags


class Notebook:
    """ Представляет собой коллекцию заметок,
     которые можно изменять, осуществлять по ним поиск и назначать им тэги"""

    def __init__(self):
        """Создает блокнот с пустым листом"""
        self.notes = []

    
    # def __repr__(self):
    #     return ', '.join(self.notes)

    
    def new_note(self, memo, tags = ''):
        """Добавляет в список заметок новую"""
        self.notes.append(Note(memo, tags))


    def _find_note(self, note_id):
        """Находит заметку по заданному идентификатору"""
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None 


    def modify_memo(self, note_id, memo):
        """Осуществляет поиск по заметкам в списке по уникальному идентификатору"""
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False
    

    def modify_tags(self, note_id, tags):
        """ Находит заметку с данным id и меняет тэг на значение агрумента данной функции"""
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False
        

    def search(self, filter):
        """ Находит все заметки по заданной строке-фильтру"""
        return [note for note in self.notes if note.match(filter)]
            
    

if __name__ == "__main__":
    n = Notebook()
    n.new_note("hello world")
    n.new_note("hello again")
    n.modify_memo(1, 'hi world')
    print(n.notes[0].memo)