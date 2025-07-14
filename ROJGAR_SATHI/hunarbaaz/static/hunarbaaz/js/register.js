
    document.addEventListener('DOMContentLoaded', function () {
      const skillSelect = document.getElementById('id_skill')
      const locationSelect = document.getElementById('id_location')
    
      const otherSkillField = document.getElementById('field-other_skill')
      const otherLocationField = document.getElementById('field-other_location')
    
      function toggleOtherSkill() {
        if (skillSelect.value === 'Others') {
          otherSkillField.style.display = 'block'
        } else {
          otherSkillField.style.display = 'none'
          document.getElementById('id_other_skill').value = ''
        }
      }
    
      function toggleOtherLocation() {
        if (locationSelect.value === 'other') {
          otherLocationField.style.display = 'block'
        } else {
          otherLocationField.style.display = 'none'
          document.getElementById('id_other_location').value = ''
        }
      }
    
      skillSelect.addEventListener('change', toggleOtherSkill)
      locationSelect.addEventListener('change', toggleOtherLocation)
    
      // Run once on load in case form is pre-filled
      toggleOtherSkill()
      toggleOtherLocation()
    })

/* auto update wage after skill selection */
// document.addEventListener("DOMContentLoaded", () => {
//   const skillSelect  = document.querySelector("#id_skill");
//   const wageInput    = document.querySelector("#id_wages");

//   const defaultWages = {{ DEFAULT_WAGES_PER_HOUR|json_script:"wageMap" }};  // Django 3.1+

//   skillSelect.addEventListener("change", () => {
//     const skill = skillSelect.value;
//     if (defaultWages[skill]) {
//       wageInput.value = defaultWages[skill];
//     }
//   });
// });

