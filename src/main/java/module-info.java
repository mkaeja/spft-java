module com.github.neuralabc.spft {
    requires org.slf4j;
    requires java.desktop;
    requires org.yaml.snakeyaml;
    requires java.prefs;
    requires forms.rt;
    requires logback.classic;

    exports com.github.neuralabc.spft.task.config to org.yaml.snakeyaml;
}