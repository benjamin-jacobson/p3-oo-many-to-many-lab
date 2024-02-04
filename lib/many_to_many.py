class Author:

    all_authors = []
    def __init__(self,name):
        self.name = name
        Author.all_authors.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name,str):
            raise Exception('Authur instance attibute name needs to be a string.')
        self._name = name

    def contracts(self):
        '''return a list of related contracts.'''
        return [c for c in Contract.all_contracts if c.author == self] # Need to undestand why self instead of self.name .. author in Contract class is author instance
    
    def books(self):
        '''should return a list of related books using the Contract class as an intermediary.'''
        return [c.book for c in Contract.all_contracts if c.author == self] # after checking that that author is class author, returns the contract book attriubte

    def sign_contract(author, book, date, royalties):
        '''create and return a new Contract object between the author and the specified book with the specified date and royalties'''
        obj = Contract(author,book,date,royalties)
        return obj

    def total_royalties(self):
        '''should return the total amount of royalties that the author has earned from all of their contracts.'''
        return sum([c.royalties for c in Contract.all_contracts if c.author == self])


class Book:

    all_books = []

    def __init__(self,title):
        self.title = title
        Book.all_books.append(self)

        @property
        def title(self):
            return self._title
        
        @title.setter
        def title(self, title):
            if not isinstance(title,str):
                raise Exception('Book instance attibute title needs to be a string.')
            self._title = title

    def contracts(self):
        '''return a list of related contracts.'''
        return [c for c in Contract.all_contracts if c.book == self] # Need to undestand why self instead of self.name .. author in Contract class is author instance
    
    def authors(self):
        '''return a list of related contracts.'''
        return [c.author for c in Contract.all_contracts if c.book == self] # Need to undestand why self instead of self.name .. author in Contract class is author instance
     
class Contract:

    all_contracts = []

    def __init__(self,author,book,date,royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author,Author):
            raise Exception('Contract attibute author must be an instance of the Author class')
        self._author = author

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if not isinstance(book,Book):
            raise Exception('Contract attibute book must be an instance of the Book class')
        self._book = book

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if not isinstance(date,str):
            raise Exception('Book instance attibute date needs to be a string.')
        self._date = date


    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties,int):
            raise Exception('Book instance attibute royalties needs to be a int.')
        self._royalties = royalties

    @classmethod
    def contracts_by_date(cls,wanted_date):
        '''should return all contracts that have the same date as the date passed into the method.'''
        return [c for c in cls.all_contracts if c.date == wanted_date]


    # @classmethod -- solution failstoo
    # def contracts_by_date(cls, date):
    #     return [contract for contract in cls.all if contract.date == date]