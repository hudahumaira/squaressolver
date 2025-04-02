# squares solver 


def load_dictionary(file_path):
    """
    this function loads a dictionary file, containing one word per line, and filters out words that:
      - are shorter than 4 or longer than 11 letters
      - contain non-alphabetic characters
    and then all words are converted to a lowercase and added to a set

    returns:
        a set containing all valid words
    """
    words = set()
    with open(file_path, 'r') as file:
        for line in file:
            #remove whitespace and convert to lowercase
            word = line.strip().lower()
            #apply the filters mentioned above
            if 4 <= len(word) <= 11 and word.isalpha():
                #add the valid word to the set
                words.add(word)
    return words

#node class for trie
class TrieNode:
    def __init__(self):
        #dictionary to store child nodes
        self.children = {}
        #flag to indicate the end of a word
        self.end_of_word = False

def build_trie(words):
    """
    this function builds a trie from a set of words

    returns:
      the root of the trie
    """
    root = TrieNode()
    for word in words:
        node = root
        for letter in word:
            if letter not in node.children:
                #create new child if letter is not present in the children
                node.children[letter] = TrieNode()
            #move to the child node
            node = node.children[letter]
        #then mark the end of the word
        node.end_of_word = True
    return root

def find_words(board, trie_root):
    """
    this function finds all words on the board using DFS with backtracking
    
    board: it is a 4x4 list of lists of letters
    trie_root: the root of the trie 
    
    returns:
      the set of found words
    """
    rows, cols = len(board), len(board[0])
    found_words = set()
    
    #the game allows to move in eight directions - up, down, left, right & diagonal
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    def dfs(i, j, node, path, visited):
        #check if the current cell is out of bounds or already visited
        if i < 0 or i >= rows or j < 0 or j >= cols:
            return
        if (i, j) in visited:
            return
        
        letter = board[i][j].lower()
        #stop if current letter is not in the trie
        if letter not in node.children:
            return
        
        #mark the cell as visited
        visited.add((i, j))
        #move to next node
        node = node.children[letter]
        #append letter to the path
        new_path = path + letter
        
        #if path is a valid word, add it to the set
        if len(new_path) >= 4 and node.end_of_word:
            found_words.add(new_path)
        
        #explore all directions recursively 
        for di, dj in directions:
            dfs(i + di, j + dj, node, new_path, visited)
        
        #backtracking: unmark the visited cell
        visited.remove((i, j))
    
    #start DFS from every cell on board
    for i in range(rows):
        for j in range(cols):
            dfs(i, j, trie_root, "", set())
    
    return found_words

def group_words_by_length(words):
    """
    this function groups words by their length
    
    returns:
     a dictionary mapping word length to a list of words
    """
    groups = {}
    for word in words:
        #add word to the corresponding group
        groups.setdefault(len(word), []).append(word)
    return groups

def main():
    #load the dictionary file
    dictionary_file = "dictionary.txt" 
    words_set = load_dictionary(dictionary_file)
    
    #build trie
    trie_root = build_trie(words_set)
    
    #define a 4x4 board
    board = [
        ['I', 'A', 'K', 'W'],
        ['F', 'R', 'I', 'T'],
        ['U', 'E', 'A', 'A'],
        ['J', 'L', 'L', 'G']
    ]
    
    #find all valid words on the board that exist in dictionary
    found_words = find_words(board, trie_root)
    
    #group words by length
    groups = group_words_by_length(found_words)
    
    #print results
    for length in sorted(groups.keys()):
        words_list = sorted(groups[length])
        print(f"{length}-letter words ({len(words_list)} words):")
        print(words_list)
        print()

if __name__ == "__main__":
    main()
