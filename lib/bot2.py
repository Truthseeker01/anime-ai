from lib.models import Recommendations

class AnimeAI:

    def __init__(self):
       self.user_input = ''
    #    DadJoke.create_table()

    def run(self):
        print("Hello and welcome to dad jokes 3")
        self.main_menu()

    def main_menu(self):
        print("Main menu")
        print("1. Want anime recommendations?")
        print("2. Talk to me about anime")
        print("3. My favorite animes")
        print('4. Exit program')

        while self.user_input not in ['1', '2', '3', '4']:
            self.user_input = input(">>>")
            if self.user_input not in ['1', '2', '3', '4']:
               print("invalid option")
            if self.user_input == '1':
               self.anime_recommendations()

            if self.user_input == '2':
               self.chat_about_anime()

            if self.user_input == '3':
               self.delete_dad_joke()

            if self.user_input == '4':
               self.exit_program()


    def anime_recommendations(self):
      all_animes = Recommendations.read_all()
      for anime in all_animes:
         print(f'\n {anime[0]}. {anime[1]}')
      self.user_input = ''

    def chat_about_anime(self):
      print('Add a joke')
      self.user_input = input('>>>')
      new_joke = DadJoke(content=self.user_input)
      new_joke.create()
      print('added')

    def delete_dad_joke(self):
      all_jokes = DadJoke.read_all()
      print('Choose a joke id to delete')
      self.user_input = input('>>>')
      while self.user_input not in [str(j[0]) for j in all_jokes]:
         print('invalid id!')
         self.user_input = input('>>>')
      DadJoke.delete_by_id(self.user_input)
      print('Deleted!')
      self.user_input = ''
          
    def exit_program(self):
       print('see ya later!')
        
