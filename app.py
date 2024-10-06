import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="3D Trainer", page_icon="🏋️")

# Function to load 3D human model for the selected exercise
def load_3d_exercise_model(exercise):
    return f"""
    <div id="{exercise.lower()}-container" style="height: 400px;"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container{exercise} = document.getElementById('{exercise.lower()}-container');
        const scene{exercise} = new THREE.Scene();
        const camera{exercise} = new THREE.PerspectiveCamera(75, container{exercise}.clientWidth / container{exercise}.clientHeight, 0.1, 1000);
        const renderer{exercise} = new THREE.WebGLRenderer({{ antialias: true }}); 
        renderer{exercise}.setSize(container{exercise}.clientWidth, container{exercise}.clientHeight);
        container{exercise}.appendChild(renderer{exercise}.domElement);

        // Lighting setup
        const ambientLight = new THREE.AmbientLight(0x404040);
        scene{exercise}.add(ambientLight);
        const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
        directionalLight.position.set(1, 1, 1).normalize();
        scene{exercise}.add(directionalLight);

        // Materials
        const skinMaterial = new THREE.MeshPhongMaterial({{color: 0xF5D3C8}});
        const clothMaterial = new THREE.MeshPhongMaterial({{color: 0x3498DB}});

        // Create human figure
        const human = new THREE.Group();

        // Torso
        const torso = new THREE.Mesh(new THREE.CylinderGeometry(0.25, 0.2, 0.6, 32), clothMaterial);
        human.add(torso);

        // Head
        const head = new THREE.Mesh(new THREE.SphereGeometry(0.15, 32, 32), skinMaterial);
        head.position.y = 0.5;
        human.add(head);

        // Arms and Legs Setup
        const upperArmGeometry = new THREE.CylinderGeometry(0.05, 0.05, 0.3, 32);
        const lowerArmGeometry = new THREE.CylinderGeometry(0.04, 0.04, 0.3, 32);
        const upperLegGeometry = new THREE.CylinderGeometry(0.07, 0.06, 0.4, 32);
        const lowerLegGeometry = new THREE.CylinderGeometry(0.05, 0.05, 0.4, 32);

        // Left and Right Limbs
        const leftUpperArm = new THREE.Mesh(upperArmGeometry, skinMaterial);
        const rightUpperArm = new THREE.Mesh(upperArmGeometry, skinMaterial);
        const leftUpperLeg = new THREE.Mesh(upperLegGeometry, clothMaterial);
        const rightUpperLeg = new THREE.Mesh(upperLegGeometry, clothMaterial);
        const leftLowerArm = new THREE.Mesh(lowerArmGeometry, skinMaterial);
        const rightLowerArm = new THREE.Mesh(lowerArmGeometry, skinMaterial);
        const leftLowerLeg = new THREE.Mesh(lowerLegGeometry, clothMaterial);
        const rightLowerLeg = new THREE.Mesh(lowerLegGeometry, clothMaterial);

        // Positions
        leftUpperArm.position.set(-0.3, 0.2, 0);
        rightUpperArm.position.set(0.3, 0.2, 0);
        leftUpperLeg.position.set(-0.1, -0.5, 0);
        rightUpperLeg.position.set(0.1, -0.5, 0);

        leftLowerArm.position.y = -0.3;
        rightLowerArm.position.y = -0.3;
        leftLowerLeg.position.y = -0.4;
        rightLowerLeg.position.y = -0.4;

        leftUpperArm.add(leftLowerArm);
        rightUpperArm.add(rightLowerArm);
        leftUpperLeg.add(leftLowerLeg);
        rightUpperLeg.add(rightLowerLeg);

        human.add(leftUpperArm, rightUpperArm, leftUpperLeg, rightUpperLeg);

        scene{exercise}.add(human);
        camera{exercise}.position.z = 3;
        camera{exercise}.position.y = 1;

        // Animation based on exercise
        function animate{exercise}() {{
            requestAnimationFrame(animate{exercise});
            const time = Date.now() * 0.001;

            // Movement based on exercise
            if ('{exercise}' === 'Squat') {{
                const squatDepth = Math.sin(time * 2) * 0.2;
                human.position.y = squatDepth;
                leftUpperLeg.rotation.x = rightUpperLeg.rotation.x = -squatDepth * 2;
            }} else if ('{exercise}' === 'PushUp') {{
                const pushUpHeight = Math.sin(time * 3) * 0.1;
                human.position.y = -0.7 + pushUpHeight;
                leftUpperArm.rotation.x = rightUpperArm.rotation.x = Math.PI / 2 - pushUpHeight * 3;
            }} else if ('{exercise}' === 'JumpingJacks') {{
                const jumpHeight = Math.sin(time * 3) * 0.1;
                human.position.y = jumpHeight;
                leftUpperArm.rotation.z = rightUpperArm.rotation.z = Math.PI / 4 * jumpHeight * 3;
                leftUpperLeg.rotation.x = rightUpperLeg.rotation.x = -Math.PI / 6 * jumpHeight * 3;
            }} else if ('{exercise}' === 'ArmCircles') {{
                const armCircleRotation = time * 3;
                leftUpperArm.rotation.z = rightUpperArm.rotation.z = armCircleRotation;
            }}

            renderer{exercise}.render(scene{exercise}, camera{exercise});
        }}
        animate{exercise}();
    </script>
    """

# Main app
def main():
    # App Header with Project Name
    st.markdown(
        """
        <div style='text-align: center; padding: 20px; background-color: #1F77B4; color: white; border-radius: 10px;'>
            <h1>InfoFit: Learn and Master Your Exercises!</h1>
            <p>Your ultimate virtual guide to exercise with 3D models and posture tips.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Adding CSS for cards and general styling
    st.markdown(
        """
        <style>
        body {
            background-color: #F0F4F8;
        }
        .card {
            padding: 20px;
            margin: 15px;
            border-radius: 15px;
            box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1);
            background-color: #ffffff;
            border: 2px solid #1F77B4;
        }
        .card-title {
            font-size: 26px;
            color: #1F77B4;
            margin-bottom: 10px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .tips {
            font-size: 16px;
            color: #666;
        }
        .section-title {
            font-size: 30px;
            color: #1F77B4;
            margin-top: 40px;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='section-title'>Exercises and 3D Models</div>", unsafe_allow_html=True)

    # List of exercises
    exercises = ["Squat", "PushUp", "JumpingJacks", "ArmCircles"]

    # Columns to display cards
    cols = st.columns(2)

    for i, exercise in enumerate(exercises):
        with cols[i % 2]:
            st.markdown(f"<div class='card'><div class='card-title'>{exercise}</div>", unsafe_allow_html=True)
            components.html(load_3d_exercise_model(exercise), height=450)

            # Tips for each exercise
            st.markdown("<div class='tips'>Correct Posture Tips:</div>", unsafe_allow_html=True)
            if exercise == "Squat":
                st.write("- Keep your back straight")
                st.write("- Knees in line with toes")
                st.write("- Lower until thighs are parallel to the ground")
            elif exercise == "PushUp":
                st.write("- Keep body in a straight line")
                st.write("- Hands slightly wider than shoulder-width")
                st.write("- Lower chest to ground, then push back up")
            elif exercise == "JumpingJacks":
                st.write("- Keep feet together and arms at your side to start")
                st.write("- Jump, raising arms and separating feet")
            elif exercise == "ArmCircles":
                st.write("- Stretch arms straight out to the sides")
                st.write("- Rotate arms in small circles")

if __name__ == "__main__":
    main()
