import Deck
import Card
import Hand
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# main class where everything is run from
# list methods: extend, insert, append, remove
#special methods:
# compare_two_hands_return_a_hand: this method returns a hand  instead of a number for a compare_hand method in Hand
# find_winnner: finds the greatest hand out of them all then checks later in the code if there are any as good

def make_row(im1, im2, im3, im4, im5):
    img1 = Image.open(im1)
    img2 = Image.open(im2)
    img3 = Image.open(im3)
    img4 = Image.open(im4)
    img5 = Image.open(im5)
    row = Image.new('RGB', (img1.width * 6, min(img1.height, img2.height)))
    row.paste(img1, (0, 0))
    row.paste(img2, (img1.width, 0))
    row.paste(img3, ((img1.width + img2.width), 0))
    row.paste(img4, ((img1.width + img2.width + img3.width), 0))
    row.paste(img5, ((img1.width + img2.width + img3.width + img4.width), 0))
    return row


def make_column(img1, img2, img3, img4):
    column = Image.new('RGB', (img1.width, img1.height * 4))
    column.paste(img1, (0, 0))
    column.paste(img2, (0, img1.height))
    column.paste(img3, (0, (img1.height + img2.height)))
    column.paste(img4, (0, (img1.height + img2.height + img3.height)))

    return column


def compare_two_hands_return_a_hand(Hand1, Hand2):
    winner1 = Hand1.compare_hand(Hand2)
    if winner1 == 1:
        return Hand1
    elif winner1 == -1:
        return Hand2
    else:
        return Hand1


def find_winner(Hand1, Hand2, Hand3, Hand4):
    y = compare_two_hands_return_a_hand(Hand1, Hand2)
    x = compare_two_hands_return_a_hand(Hand3, Hand4)
    return compare_two_hands_return_a_hand(x, y)


if __name__ == "__main__":
    tied = []
    winners = []
    poker_game = []
    deck = Deck.Deck()
    deck.shuffle()
    for i in range(4):
        poker_game.append(Hand.Hand())
    for i in range(5):
        poker_game[0].add_card(deck.deal_card())
        poker_game[1].add_card(deck.deal_card())
        poker_game[2].add_card(deck.deal_card())
        poker_game[3].add_card(deck.deal_card())
    winner = find_winner(poker_game[0], poker_game[1], poker_game[2], poker_game[3])
    winners.append(winner)
    winner_pos = poker_game.index(winner)
    poker_game.remove(winner)
    for i in poker_game:
        if winner.compare_hand(i) == 0:
            tied.append(i)
    winners.extend(tied)
    poker_game.insert(winner_pos, winner)
    print(poker_game)
    print(winners)
    row1 = make_row(poker_game[0].get_hand()[0].image_file_name(), poker_game[0].get_hand()[1].image_file_name(),
                    poker_game[0].get_hand()[2].image_file_name(), poker_game[0].get_hand()[3].image_file_name(),
                    poker_game[0].get_hand()[4].image_file_name())
    row2 = make_row(poker_game[1].get_hand()[0].image_file_name(), poker_game[1].get_hand()[1].image_file_name(),
                    poker_game[1].get_hand()[2].image_file_name(), poker_game[1].get_hand()[3].image_file_name(),
                    poker_game[1].get_hand()[4].image_file_name())
    row3 = make_row(poker_game[2].get_hand()[0].image_file_name(), poker_game[2].get_hand()[1].image_file_name(),
                    poker_game[2].get_hand()[2].image_file_name(), poker_game[2].get_hand()[3].image_file_name(),
                    poker_game[2].get_hand()[4].image_file_name())
    row4 = make_row(poker_game[3].get_hand()[0].image_file_name(), poker_game[3].get_hand()[1].image_file_name(),
                    poker_game[3].get_hand()[2].image_file_name(), poker_game[3].get_hand()[3].image_file_name(),
                    poker_game[3].get_hand()[4].image_file_name())

    column = make_column(row1, row2, row3, row4)
    draw = ImageDraw.Draw(column)
    for i in range(4):
        text = poker_game[i].get_hand_type()
        for x in winners:
            if x == poker_game[i]:
                text = f'{poker_game[i].get_hand_type()} \n WINNER'
        draw.text((510, (150 * i) + 50), text)
    column.show()
    # images.show()
