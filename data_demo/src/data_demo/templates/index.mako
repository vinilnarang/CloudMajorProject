<%!from desktop.views import commonheader, commonfooter %>
<%namespace name="shared" file="shared_components.mako" />

${commonheader("Data Demo", "data_demo", user, "100px")}
${shared.menubar(section='mytab')}

## Use double hashes for a mako template comment
## Main body

<div class="container-fluid">
  <h2>Data Demo app is successfully setup!</h2>
  <p>It's now ${date}.</p>
</div>
${commonfooter(messages)}
