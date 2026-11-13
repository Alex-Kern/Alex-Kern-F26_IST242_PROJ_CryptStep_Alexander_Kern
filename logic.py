"""Pure game logic for CryptStep. Decoupled from Pygame."""


def try_move(pos, direction, walls, bounds):
    """Attempt to move an entity by (dx, dy) within grid bounds and wall constraints."""
    pass


def resolve_combat(player_hp, damage):
    """Apply damage to player health, flooring cleanly at 0."""
    pass


def check_game_state(player_pos, exit_pos, relics_collected, total_relics, player_hp):
    """Return current game status: 'PLAYING', 'WON', or 'LOST'."""
    pass