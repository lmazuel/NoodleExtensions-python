import NoodleExtensions

# Setting up an editor object
editor = NoodleExtensions.Editor(r"C:\Program Files (x86)\Steam\steamapps\common\Beat Saber\Beat Saber_Data\CustomWIPLevels\ExampleLevel\EasyStandard.dat")

# Setting up an animator object
animator = NoodleExtensions.Animator(editor)

# Let's say we want a note to fall from the sky and bounce.
#  We would put it in a track;
editor.EditBlock(6, (1, 0), "BounceTrack")

# Then we would animate it to do so!
animator.Animate("AnimateTrack", NoodleExtensions.Animations.position, [
    [0, 10, 0, 0],
    [0, 0, 0, 1, "easeOutBounce"]
], "BounceTrack", 5, 6)

# This script is really this easy.