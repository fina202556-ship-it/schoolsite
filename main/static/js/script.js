document.addEventListener("DOMContentLoaded", () => {
// add student preview
    const addInput = document.getElementById("image");
    const addPreview = document.getElementById("add_preview");
    if (addInput) {
        addInput.addEventListener("change", () => {
            const file = addInput.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = e => addPreview.src = e.target.result;
                reader.readAsDataURL(file);
            } else {
                addPreview.src = "/static/uploads/default_avatar.png";
            }
        });
    }

    // edit modal preview
    const editButtons = document.querySelectorAll(".edit-btn");
    const form = document.getElementById("editStudentForm");
    const imageInput = document.getElementById("edit_image");
    const preview = document.getElementById("edit_preview");

    editButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            document.getElementById("edit_id").value = btn.dataset.id;
            document.getElementById("edit_name").value = btn.dataset.name;
            document.getElementById("edit_student_number").value = btn.dataset.studentNumber;
            document.getElementById("edit_phone").value = btn.dataset.phone;
            document.getElementById("edit_address").value = btn.dataset.address;
            document.getElementById("edit_birthday").value = btn.dataset.birthday;
            document.getElementById("edit_country").value = btn.dataset.country;

            preview.src = btn.dataset.image
                ? `/static/uploads/${btn.dataset.image}`
                : '/static/uploads/default_avatar.png';

            form.action = `/update_student/${btn.dataset.id}`;
        });
    });

    if (imageInput) {
        imageInput.addEventListener("change", () => {
            const file = imageInput.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = e => preview.src = e.target.result;
                reader.readAsDataURL(file);
            } else {
                preview.src = "/static/uploads/default_avatar.png";
            }
        });
    }
});
